# vosper: a simple tool to easily get high-quality Automatic Speech Recognition using SOTA models
import vosper, os; vosper = vosper.new()

while 'listening':
    text = vosper.listen()
    if ('-' in text): print(text)
    elif (text != ''): os.system('clear'); print('- '+ text)
