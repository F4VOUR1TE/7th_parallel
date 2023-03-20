from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDTextButton
from kivymd.uix.button import MDFlatButton
from kivy.uix.modalview import ModalView
from kivymd.uix.fitimage import FitImage
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<AuthorizationScreen>:
    MDScreen:
        FitImage:
            source : 'pic/bg.png'
        MDTextField:
            hint_text: "Введите ваш номер телефона"
            font_name : 'Montserrat2.ttf'
            mode: "fill"
            fill_color: 0, 0, 0, 0.4
            pos_hint:{"center_x": 0.5, "center_y": 0.5}

        MDRoundFlatButton:
            text:"Авторизоваться"
            font_size: "38sp"
            text_color : 'black'
            pos_hint:{"center_x": 0.5, "center_y": 0.15}
            md_bg_color : '32B68F'
            font_name : 'Montserrat2.ttf'
            on_press: root.manager.current = 'main'
<MainMenu>:
    MDScreen:
        FitImage:
            source : 'pic/1bg.png'
                    
        MDRoundFlatButton:
            text:"Сканировать"
            font_size: "38sp"
            text_color : 'black'
            pos_hint:{"center_x": 0.5, "center_y": 0.15}
            md_bg_color : '32B68F'
            font_name : 'Montserrat2.ttf'
                         
                 
        MDRoundFlatButton:
            text:"?"
            font_size: "37sp"
            text_color : 'black'
            pos_hint:{"center_x": 0.91, "center_y": 0.95}
            md_bg_color : '32B68F'
            font_name : 'Montserrat2.ttf'
            on_press: root.manager.current = 'info'
                 
        MDIconButton:
            icon:"pic/gift.png"    
            pos_hint:{"center_x": 0.03, "center_y": 0.96}
            on_press: root.manager.current = 'gift'
                         
                 
        MDRoundFlatButton
            text : "100 баллов"
            pos_hint:{"center_x": 0.5, "center_y": 0.422}
            text_color : 'black'
            font_size: "34sp"
            md_bg_color : (0,0,0,0)
            font_name : 'Montserrat2.ttf'
            
               
        Image:
            source : 'pic/user.png'
            pos_hint:{"center_x": 0.5, "center_y": 0.65}
            size_hint :  (.3, .3)

<GiftScreen>
    MDScreen:
        FitImage:
            source : 'pic/bg.png'
        Image:
            source : 'pic/Bear.png'
            pos_hint:{"center_x": 0.73, "center_y": 0.1}
            size_hint :  (.6, .6)
        MDLabel:
            text: "Подарки"
            font_name : 'Montserrat2.ttf'
            pos_hint:{"center_x": 0.85, "center_y": 0.95}
            theme_text_color: "Custom"
            text_color: 'black'
            font_size: "34sp"
            bold: True
        MDIconButton:
            icon:"pic/cross.png"    
            pos_hint:{"center_x": 0.03, "center_y": 0.98}
            on_press: root.manager.current = 'main'
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.25, "center_y": 0.7}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.50, "center_y": 0.7}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.75, "center_y": 0.7}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11    
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.25, "center_y": 0.55}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.50, "center_y": 0.55}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.75, "center_y": 0.55}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11 
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.25, "center_y": 0.4}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.50, "center_y": 0.4}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.75, "center_y": 0.4}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'pic/gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11 
<InfoScreen>:
    MDScreen:
        FitImage:
            source : 'pic/bg2.png'
        MDIconButton:
            icon:"pic/cross.png"    
            pos_hint:{"center_x": 0.03, "center_y": 0.98}
            on_press: root.manager.current = 'main'
        MDLabel:
            text: 'Это приложение создано, для того чтобы люди которые заботятся об окружающей среде и планете, получали бонусы за каждую сданную бутылку. Для того чтобы начать копить баллы на подарки, вам необходимо нажать на кнопку "Сканировать" и сделать 2 фотографии: первую, как вы вставили бутылку и вторую, как аппарат принял бутылку. После чего вы получите 1 балл за каждую сданную бутылку. Далее при накоплении баллов вы можете зайти в раздел "Подарки" и посмотреть сколько вам осталось накопить.'
            font_name : 'Montserrat2.ttf'
            pos_hint:{"center_x": 0.51, "center_y": 0.73}
            theme_text_color: "Custom"
            text_color: 'black'
            font_size: "19sp"
            bold: True
        MDLabel:
            text: 'За остальными вопросами обращайтесь по телефону +7 995 888 88 88 Или пишите в наши соц.сети:'
            font_name : 'Montserrat2.ttf'
            pos_hint:{"center_x": 0.51, "center_y": 0.20}
            theme_text_color: "Custom"
            text_color: 'black'
            font_size: "19sp"
            bold: True
        MDLabel:
            text: 'Вк - @pasha ne chudi'
            font_name : 'Montserrat2.ttf'
            pos_hint:{"center_x": 0.51, "center_y": 0.11}
            theme_text_color: "Custom"
            text_color: 'black'
            font_size: "19sp"
            bold: True
        MDLabel:
            text: 'Телеграм - @pasha ne chudi'
            font_name : 'Montserrat2.ttf'
            pos_hint:{"center_x": 0.51, "center_y": 0.08}
            theme_text_color: "Custom"
            text_color: 'black'
            font_size: "19sp"
            bold: True
                
""")

class MainMenu(MDScreen):
     pass
    
class AuthorizationScreen(MDScreen):
     pass

class GiftScreen(MDScreen):
     pass

class InfoScreen(MDScreen):
     pass
class EcoBottle(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AuthorizationScreen(name='auth'))
        sm.add_widget(MainMenu(name='main'))
        sm.add_widget(GiftScreen(name='gift'))
        sm.add_widget(InfoScreen(name='info'))
        
        self.theme_cls.primary_palette = "Green"
        #self.theme_cls.theme_style = "Dark"


        # button_ball_pos_x = 0.5
        # button_ball_pos_y = 0.5
        Window.size = (400, 750)

        return (
            sm
        )


EcoBottle().run()