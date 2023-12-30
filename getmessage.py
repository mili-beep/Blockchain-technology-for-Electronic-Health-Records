
def get_message(filepath):
    with open(filepath, 'rb') as file:
        document_data = file.read()
    return document_data