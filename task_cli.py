import cmd

class TaskShell(cmd.Cmd):
    intro = 'Welcome to Task Tracker Application. Type help or ? to list commands.\n'
    prompt = '(task_tracker) '

    def do_add(self, arg):
        'Add a new task to track. Usage: add <task>'
        print(f'Arg: {arg}')

    def do_bye(self, arg):
        'Exit the CLI'
        print('Thank you for using ')
        return True

if __name__ == '__main__':
    TaskShell().cmdloop()
