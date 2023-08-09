from behave import *
from todolist import ToDoList

@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = ToDoList()

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['Task'])

@when('the user adds a task "{description}"')
def step_impl(context, description):
    context.todo_list.add_task(description)

@when('the user lists all tasks')
def step_impl(context):
    context.output = []
    for task in context.todo_list.tasks:
        context.output.append(str(task))

@when('the user marks task "{description}" as completed')
def step_impl(context, description):
    context.todo_list.mark_completed(description)

@when('the user removes task "{description}"')
def step_impl(context, description):
    context.todo_list.remove_task(description)

@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list.clear_list()

@then('the to-do list should contain "{description}"')
def step_impl(context, description):
    assert any(task.description == description for task in context.todo_list.tasks)

@then('the output should contain')
def step_impl(context):
    expected_output = context.output
    assert context.output == expected_output

@then('the to-do list should show task "{description}" as completed')
def step_impl(context, description):
    assert any(task.description == description and task.status == 'Completed' for task in context.todo_list.tasks)

@then('the to-do list should not contain "{description}"')
def step_impl(context, description):
    assert not any(task.description == description for task in context.todo_list.tasks)

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.tasks) == 0
