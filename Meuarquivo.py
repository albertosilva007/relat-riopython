import pandas as pd
import win32com.client as win32


# importar a base de dados

tabela_vendas = pd.read_excel('Vendas.xlsx')
print(tabela_vendas)

# visualizar a base de dados

pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)


# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)


print('-' * 50)
# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)

# enviar um email com o relatório
outlook = win32.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)
message.Display()
message.To = 'pr.josealbertoibc@gmail.com'
message.Subject = 'Relatório de Vendas por Loja'
message.HTMLBody = f'''

<p>Prezados,</q>



<p>segue o relátorio de vendas por cada loja.</p>

<p>Faturamento:</p> 
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}


<p>Qualquer duvida estou á disposição.</p>


<p>Att,.</p> 
<p>Alberto Silva</p>

'''







