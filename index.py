import pyautogui as pa
import pandas as pd

pa.PAUSE=4

try:
    vendas_df = pd.read_excel('C:\\Users\\carro_akq51l3\\Downloads\\Cópia de Vendas.xlsx')
    print(vendas_df.shape())
except:
    pa.hotkey('win')
    pa.write('chrome')
    pa.hotkey('enter')
    pa.click(x=1287, y=147)
    pa.click(x=1174, y=552)
    pa.doubleClick(400, 285)
    pa.click(x=1267, y=447)
    pa.click(x=996, y=383)
