# Global scope and local scope

var_global = 'Complete Python Course'

def write_text():
    global  var_global
    var_global = 'database with SQL'
    var_local = 'Jose Junior'
    print(f'Var global: {var_global}')
    print(f'Var local: {var_local}')

if __name__ == '__main__':
    print(f'Execute the function write_text(): ')
    write_text()

    print('Try to access the variables directly.')
    print(f'Var global: {var_global}')
    # print(f'Var local: {var_local}')



