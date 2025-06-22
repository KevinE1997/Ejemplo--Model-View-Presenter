import tkinter as tk

class Model:
    def __init__(self):
        self.count = 0

class View:
    def __init__(self, root, presenter):
        self.presenter = presenter
        self.label = tk.Label(root, text="Contador: 0")
        self.label.pack()
        self.button = tk.Button(root, text="Incrementar", command=self.presenter.increment)
        self.button.pack()

    def update_count(self, count):
        self.label.config(text=f"Contador: {count}")

class Presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def increment(self):
        self.model.count += 1
        self.view.update_count(self.model.count)

root = tk.Tk()
root.title("MVP Demo")
model = Model()
presenter = Presenter(None, model)
view = View(root, presenter)
presenter.view = view

root.mainloop()
