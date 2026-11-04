from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.title = "Калькулятор на Kivy"
        
        # Головний контейнер
        root_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Поле виведення результату / вводу
        self.solution = TextInput(
            text="0", 
            font_size=40, 
            halign="right", 
            readonly=True, 
            size_hint=(1, 0.25)
        )
        root_layout.add_widget(self.solution)
        
        # Кнопки калькулятора
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=10)
            for label in row:
                btn = Button(
                    text=label, 
                    font_size=32,
                    background_color=(0.2, 0.6, 0.8, 1)
                )
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            root_layout.add_widget(h_layout)
            
        # Кнопка дорівнює (=)
        equals_btn = Button(
            text="=", 
            font_size=32, 
            size_hint=(1, 0.2),
            background_color=(0.2, 0.8, 0.3, 1)
        )
        equals_btn.bind(on_press=self.on_solution)
        root_layout.add_widget(equals_btn)
        
        return root_layout

    def on_button_press(self, instance):
        current = self.solution.text
        text = instance.text
        
        if text == "C":
            self.solution.text = "0"
        else:
            if current == "0":
                self.solution.text = text
            else:
                self.solution.text = current + text

    def on_solution(self, instance):
        text = self.solution.text
        try:
            # Безпечне обчислення математичного виразу
            response = str(eval(text))
            self.solution.text = response
        except Exception:
            self.solution.text = "Помилка"

if __name__ == "__main__":
    CalculatorApp().run()