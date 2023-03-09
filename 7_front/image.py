from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

# Designate Our .kv design file 
Builder.load_file('image.kv')

class MyLayout(Widget):
	def hello_on(self):
		
		self.ids.my_image.source = '+.png'

	# def hello_off(self):
	# 	self.ids.my_image.source = '+.png'
	# 	#self.ids.my_label.text = "You Pressed The Button!"
		
class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()
