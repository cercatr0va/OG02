import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Task:
    """Класс задачи с атрибутами."""
    def __init__(self, title, time, location):
        self.title = title
        self.time = time
        self.location = location
        self.done = False  # Статус задачи (выполнена или нет)

    def toggle_done(self):
        """Переключение статуса выполнения задачи."""
        self.done = not self.done

    def get_attributes(self):
        """Возвращает строковое представление атрибутов задачи."""
        status = "Сделано" if self.done else "Не сделано"
        return f"{self.title} | Время: {self.time} | Место: {self.location} | Статус: {status}"

class TaskPlanner:
    """Планировщик задач с графическим интерфейсом."""
    def __init__(self, root):
        self.root = root
        self.root.title("Планировщик задач")
        self.root.configure(bg="green")  # Основной цвет окна - зеленый

        # Список задач
        self.tasks = []

        # Создаем интерфейс
        self.create_widgets()

    def create_widgets(self):
        """Создает графические элементы."""
        # Заголовок
        self.title_label = tk.Label(self.root, text="Планировщик задач", font=("Arial", 16), bg="green")
        self.title_label.pack(pady=10)

        # Поле для ввода задачи
        self.task_entry_label = tk.Label(self.root, text="Введите название задачи:", bg="green")
        self.task_entry_label.pack(pady=5)

        self.task_entry = tk.Entry(self.root, width=40, bg="red")  # Поле ввода задачи - красное
        self.task_entry.pack(pady=5)

        # Поле для времени выполнения
        self.time_entry_label = tk.Label(self.root, text="Введите время выполнения:", bg="green")
        self.time_entry_label.pack(pady=5)

        self.time_entry = tk.Entry(self.root, width=40, bg="red")  # Поле ввода времени - красное
        self.time_entry.pack(pady=5)

        # Поле для ввода места выполнения
        self.location_entry_label = tk.Label(self.root, text="Введите место выполнения:", bg="green")
        self.location_entry_label.pack(pady=5)

        self.location_entry = tk.Entry(self.root, width=40, bg="red")  # Поле ввода места - красное
        self.location_entry.pack(pady=5)

        # Кнопка для добавления задачи
        self.add_button = tk.Button(self.root, text="Добавить задачу", command=self.add_task)
        self.add_button.pack(pady=10)

        # Список задач
        self.tasks_listbox = tk.Listbox(self.root, width=60, height=10, bg="yellow")  # Поле отображения задач - желтое
        self.tasks_listbox.pack(pady=10)

        # Кнопка для удаления задачи
        self.delete_button = tk.Button(self.root, text="Удалить задачу", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Кнопка для отметки задачи как выполненной
        self.done_button = tk.Button(self.root, text="Отметить задачу как выполненную", command=self.mark_task_done)
        self.done_button.pack(pady=5)

    def add_task(self):
        """Добавляет задачу в список."""
        title = self.task_entry.get()
        time = self.time_entry.get()
        location = self.location_entry.get()

        if not title or not time or not location:
            messagebox.showwarning("Ошибка", "Все поля должны быть заполнены.")
            return

        # Создаем задачу и добавляем в список
        new_task = Task(title, time, location)
        self.tasks.append(new_task)

        # Обновляем отображение задач
        self.update_task_listbox()

        # Очищаем поля ввода
        self.task_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)

    def delete_task(self):
        """Удаляет выбранную задачу."""
        selected_task_index = self.tasks_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Ошибка", "Пожалуйста, выберите задачу для удаления.")
            return

        del self.tasks[selected_task_index[0]]

        # Обновляем отображение задач
        self.update_task_listbox()

    def mark_task_done(self):
        """Отмечает задачу как выполненную."""
        selected_task_index = self.tasks_listbox.curselection()
        if not selected_task_index:
            messagebox.showwarning("Ошибка", "Пожалуйста, выберите задачу для отметки.")
            return

        task = self.tasks[selected_task_index[0]]
        task.toggle_done()

        # Обновляем отображение задач
        self.update_task_listbox()

    def update_task_listbox(self):
        """Обновляет список задач в интерфейсе."""
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task.get_attributes())

# Создаем основное окно
root = tk.Tk()

# Запуск приложения
app = TaskPlanner(root)
root.mainloop()
