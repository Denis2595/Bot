import tkinter as tk


class ChatBot:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chat Bot")

        self.frame = tk.Frame(self.root, width=400, height=300)
        self.frame.pack()

        self.message_label = tk.Label(self.frame, text="Введите сообщение:")
        self.message_label.pack(side=tk.LEFT)

        self.message_entry = tk.Entry(self.frame, width=30)
        self.message_entry.pack(side=tk.LEFT)

        self.send_button = tk.Button(self.frame, text="Отправить", command=self.handle_message)
        self.send_button.pack(side=tk.LEFT)

        self.response_frame = tk.Frame(self.root, width=400, height=100)
        self.response_frame.pack()

        self.response_label = tk.Label(self.response_frame, text="")
        self.response_label.pack()

        self.responses = ['Привет!', 'Денис', 'ВК: Денис Пономарев https://vk.com/bogreshnik ', 'Пожалуйста, уточните ваш запрос.']

    def handle_message(self):
        message = self.message_entry.get()
        response = self.get_response(message)
        self.display_response(response)

    def get_response(self, message):
        if message.lower() == 'привет':
            return self.responses[0]
        elif message.lower() == 'кто создатель?':
            return self.responses[1]
        elif message.lower() == 'запись':
            return self.responses[2]
        else:
            return self.responses[3]

    def display_response(self, response):
        self.response_label.config(text=response)

    def run(self):
        self.root.mainloop()


chat_bot = ChatBot()
chat_bot.run()