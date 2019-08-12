import eel

eel.init('web')

@eel.expose
def data_pass(data):
  print('Received values: {}'.format(str(data)))
  eel.log('Transmitted values: {}'.format(str(data)))

eel.start('index.html')
