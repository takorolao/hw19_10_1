from django.shortcuts import render

def task_list(request):
    tasks = ['Task 1', 'Task 2', 'Task 3']  # список задач
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = f'Task {task_id}'  # получение задачи из базы данных 
    return render(request, 'tasks/task_detail.html', {'task': task})
