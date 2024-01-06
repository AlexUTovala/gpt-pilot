import ast
import os

def generate_ast(root_dir):
    for dir_name, dirs, files in os.walk(root_dir):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(dir_name, file_name)
                with open(file_path, 'r') as file:
                    file_content = file.read()
                try:
                    tree = ast.parse(file_content)
                    save_ast_result(file_path, tree)  # Save the result of the AST
                except SyntaxError as e:
                    print(f"Syntax error in file {file_path}: {e}")

def save_ast_result(file_path, tree):
    # TODO: Implement the logic to save the result of the AST
    # You can write the tree to a file, store it in a database, or perform any other desired action
    # Example: Writing the tree to a file with the same name and a .ast extension
    ast_file_path = file_path + '.ast'
    with open(ast_file_path, 'w') as ast_file:
        ast_file.write(ast.dump(tree))

generate_ast('/Users/alexurbanec/gpt-pilot')