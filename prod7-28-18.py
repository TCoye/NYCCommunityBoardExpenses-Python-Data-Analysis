import numpy as np
import pandas as pd
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.random.seed(12345)
import matplotlib.pyplot as plt
import matplotlib
plt.rc('figure', figsize=(10, 6))
np.set_printoptions(precision=4, suppress=True)
import matplotlib as mpl
import matplotlib as mpl

df = pd.read_csv('Expense_Budget.csv')

#df.to_pickle('Expense_Budget.p')
#df = pd.read_pickle('Expense_Budget.p')
df['Adopted Budget Amount'] = df['Adopted Budget Amount'].str.replace(',', '').astype(float)

grouped_df = df[['Adopted Budget Amount', 'Agency Name','Fiscal Year']].groupby(['Fiscal Year', 'Agency Name']).sum()
grouped_df = grouped_df.reset_index()

grouped_df_qcb= grouped_df[grouped_df['Agency Name'].str.contains("QUEENS COMMUNITY BOARD ")]

df2 = grouped_df_qcb[['Adopted Budget Amount', 'Agency Name','Fiscal Year']].groupby(['Fiscal Year']).sum().reset_index()
df2 = df2.set_index('Fiscal Year')
df2

ax = df2.plot( kind='bar', stacked=True, width=.3,color=['rgb'],legend = None)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
#ax.set_title('Adopted Budget Amount', fontsize= 10,position=(.50, 1)) # title of plot
plt.xticks(rotation=0)
title_string = "Queens Community Board - Adopted Budget Amount"
plt.suptitle(title_string, y=1.02, fontsize=16)
plt.tight_layout()
plt.savefig('pltmanhattan.png',dpi = 100,bbox_inches = 'tight')
plt.show()


grouped_df_bcb= grouped_df[grouped_df['Agency Name'].str.contains("BROOKLYN COMMUNITY BOARD")]
grouped_df_bcb

df3 = grouped_df_bcb[['Adopted Budget Amount', 'Agency Name','Fiscal Year']].groupby(['Fiscal Year']).sum().reset_index()
df3 = df3.set_index('Fiscal Year')
df3

ax = df3.plot( kind='bar', stacked=True, width=.3,color=['rgb'],legend = None)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
#ax.set_title('Adopted Budget Amount', fontsize= 10,position=(.50, 1)) # title of plot
plt.xticks(rotation=0)
title_string = "Brooklyn Community Board - Adopted Budget Amount"
plt.suptitle(title_string, y=1.02, fontsize=16)
plt.tight_layout()
plt.savefig('pltmanhattan.png',dpi = 100,bbox_inches = 'tight')
plt.show()


grouped_df_sicb= grouped_df[grouped_df['Agency Name'].str.contains("STATEN ISLAND COMMUNITY BOARD")]
grouped_df_sicb

df4 = grouped_df_sicb[['Adopted Budget Amount', 'Agency Name','Fiscal Year']].groupby(['Fiscal Year']).sum().reset_index()
df4 = df4.set_index('Fiscal Year')
df4

ax = df4.plot( kind='bar', stacked=True, width=.3,color=['rgb'],legend = None)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
#ax.set_title('Adopted Budget Amount', fontsize= 10,position=(.50, 1)) # title of plot
plt.xticks(rotation=0)
title_string = "Staten Island Community Board - Adopted Budget Amount"
plt.suptitle(title_string, y=1.02, fontsize=16)
plt.tight_layout()
plt.savefig('pltmanhattan.png',dpi = 100,bbox_inches = 'tight')
plt.show()


grouped_df_bxcb= grouped_df[grouped_df['Agency Name'].str.contains("BRONX COMMUNITY BOARD")]
grouped_df_bxcb

df5 = grouped_df_bxcb[['Adopted Budget Amount', 'Agency Name','Fiscal Year']].groupby(['Fiscal Year']).sum().reset_index()
df5 = df5.set_index('Fiscal Year')
df5

ax = df5.plot( kind='bar', stacked=True, width=.3,color=['rgb'],legend = None)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
#ax.set_title('Adopted Budget Amount', fontsize= 10,position=(.50, 1)) # title of plot
plt.xticks(rotation=0)
title_string = "Bronx Community Board - Adopted Budget Amount"
plt.suptitle(title_string, y=1.02, fontsize=16)
plt.tight_layout()
plt.savefig('pltmanhattan.png',dpi = 100,bbox_inches = 'tight')
plt.show()

grouped_df_mcb= grouped_df[grouped_df['Agency Name'].str.contains("MANHATTAN COMMUNITY BOARD")]
grouped_df_mcb

df6 = grouped_df_mcb[['Adopted Budget Amount', 'Agency Name','Fiscal Year']].groupby(['Fiscal Year']).sum().reset_index()
df6 = df6.set_index('Fiscal Year')
df6

ax = df6.plot( kind='bar', stacked=True, width=.3,color=['rgb'],legend = None)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
#ax.set_title('Adopted Budget Amount', fontsize= 10,position=(.50, 1)) # title of plot
axes = plt.gca()
axes.set_ylim([0,14000000])
plt.xticks(rotation=0)
title_string = "Manhattan Community Board - Adopted Budget Amount"
plt.suptitle(title_string, y=1.02, fontsize=16)
plt.tight_layout()
plt.savefig('pltmanhattan.png',dpi = 100,bbox_inches = 'tight')
plt.show()