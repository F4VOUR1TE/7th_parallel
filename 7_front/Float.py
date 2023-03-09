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
            source : 'bg.png'
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
            source : '1bg.png'
                    
        MDRoundFlatButton:
            text:"Сканировать"
            font_size: "38sp"
            text_color : 'black'
            pos_hint:{"center_x": 0.5, "center_y": 0.15}
            md_bg_color : '32B68F'
            font_name : 'Montserrat2.ttf'
                         
                 
        MDRoundFlatButton:
            text:"?"
            font_size: "30sp"
            text_color : 'black'
            pos_hint:{"center_x": 0.93, "center_y": 0.93}
            md_bg_color : '32B68F'
            font_name : 'Montserrat2.ttf'
            on_press: root.manager.current = 'info'
                 
        MDIconButton:
            icon:"gift.png"    
            pos_hint:{"center_x": 0.03, "center_y": 0.96}
            on_press: root.manager.current = 'gift'
                         
                 
        MDRoundFlatButton
            text : "100 баллов"
            pos_hint:{"center_x": 0.5, "center_y": 0.5}
            text_color : 'black'
            font_size: "34sp"
            md_bg_color : (0,0,0,0)
            font_name : 'Montserrat2.ttf'
            
               
        Image:
            source : 'user.png'
            pos_hint:{"center_x": 0.5, "center_y": 0.75}
            size_hint :  (.2, .2)

<GiftScreen>
    MDScreen:
        FitImage:
            source : 'bg.png'
        Image:
            source : 'Bear.png'
            pos_hint:{"center_x": 0.73, "center_y": 0.1}
            size_hint :  (.6, .6)
        MDLabel:
            text: "Подарки"
            font_name : 'Montserrat2.ttf'
            pos_hint:{"center_x": 0.8, "center_y": 0.95}
            theme_text_color: "Custom"
            text_color: 'black'
            font_size: "34sp"
            bold: True
        MDIconButton:
            icon:"cross.png"    
            pos_hint:{"center_x": 0.03, "center_y": 0.95}
            on_press: root.manager.current = 'main'
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.25, "center_y": 0.7}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.50, "center_y": 0.7}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.75, "center_y": 0.7}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11    
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.25, "center_y": 0.55}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.50, "center_y": 0.55}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.75, "center_y": 0.55}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11 
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.25, "center_y": 0.4}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.50, "center_y": 0.4}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11
        Button:
			size_hint: .11, .11
			pos_hint:{"center_x": 0.75, "center_y": 0.4}
			background_color: 0,0,0,0
			Image:
				id: my_image
				source: 'gift1.png'
				center_x: self.parent.center_x
				center_y: self.parent.center_y
				size_hint: .11, .11 
<InfoScreen>:
    MDScreen:
        FitImage:
            source : 'bg2.png'
        MDIconButton:
            icon:"cross.png"    
            pos_hint:{"center_x": 0.03, "center_y": 0.95}
            on_press: root.manager.current = 'main'
                
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
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
       
        # button_ball_pos_x = 0.5
        # button_ball_pos_y = 0.5
        Window.size = (400, 750)
            
        return (
            sm
        #     MDScreen(
        
        #         FitImage(
        #             source = '1bg.png',
                    
        #         ),
        #         MDRoundFlatButton(
        #             text="Сканировать",
        #             font_size= "38sp",
        #             text_color = 'black',
        #             pos_hint={"center_x": 0.5, "center_y": 0.15},
        #             md_bg_color = '32B68F',
        #             font_name = 'Montserrat2.ttf',
        #                 #font_style = 'H3',
        #         ),
        #         MDRoundFlatButton(
        #             text="?",
        #             font_size= "30sp",
        #             text_color = 'black',
        #             pos_hint={"center_x": 0.93, "center_y": 0.93},
        #             md_bg_color = '32B68F',
        #             font_name = 'Montserrat2.ttf'
        #         ),
        #         MDIconButton(
        #             icon="Gift.png",
        #                 #size = self.parent.size,
        #             pos_hint={"center_x": 0.02, "center_y": 0.96},
        #                 # user_font_size = "24sp"
        #         ),
        #         MDRoundFlatButton(
        #             text = "100 баллов",
        #             pos_hint={"center_x": button_ball_pos_x, "center_y": button_ball_pos_y},
        #             text_color = 'black',
        #             font_size= "34sp",
        #             md_bg_color = (0,0,0,0),
        #             font_name = 'Montserrat2.ttf'
        #         ),
               
        #         Image(
        #             source = 'user.png',
        #             pos_hint={"center_x": 0.5, "center_y": 0.75},
                    
        #             size_hint =  (.2, .2)
        #         )
               
        #     )
        )


EcoBottle().run()