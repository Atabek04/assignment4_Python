import os


# 1. Write a text string to a file from Keyword.
def write_text_to_file(file_name, text):
    with open(file_name, 'w') as f:
        f.write(text)


# 2. Determine the length of the file
def file_length(file_name):
    return os.path.getsize(file_name)


# 3. Reading the file and displaying its contents on the screen
def read_and_display_file(file_name):
    with open(file_name, 'r') as f:
        print(f.read())


# 4. Replacing 10 bytes in a file
def replace_bytes_in_file(file_name, offset, new_data):
    with open(file_name, 'rb+') as f:
        f.seek(offset)
        f.write(new_data)


# 5. Read 5 bytes from the file and display it on the screen
def read_bytes_from_file(file_name, offset, length):
    with open(file_name, 'rb') as f:
        f.seek(offset)
        print(f.read(length))


# 6. Copying one file to another
def copy_file(src_file, dest_file):
    with open(src_file, 'rb') as src, open(dest_file, 'wb') as dest:
        dest.write(src.read())


# 7. Copy the file from the 20th byte to the second file
def copy_file_bytes(src_file, dest_file, offset, length):
    with open(src_file, 'rb') as src, open(dest_file, 'wb') as dest:
        src.seek(offset)
        dest.write(src.read(length))


# 8. Find the block in the file and display it on the screen
def find_and_display_block(file_name, block):
    with open(file_name, 'r') as f:
        for line in f:
            if block in line:
                print(line)


# 9. Find the block in the file and replace it
def find_and_replace_block(file_name, block, new_block):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    with open(file_name, 'w') as f:
        for line in lines:
            if block in line:
                line = line.replace(block, new_block)
            f.write(line)


# 10. Find the block in the file and write it at the end of the second file.
def find_and_write_block(file_name, block, dest_file):
    with open(file_name, 'r') as f:
        for line in f:
            if block in line:
                with open(dest_file, 'a') as dest:
                    dest.write(line)


# 11. Find a block in the file and write it without breaking the length of the second file
def find_and_write_block_fixed_length(file_name, block, dest_file, max_length):
    with open(file_name, 'r') as f:
        for line in f:
            if block in line:
                with open(dest_file, 'a') as dest:
                    if dest.tell() + len(line) <= max_length:
                        dest.write(line)
                    else:
                        break


# 12. Reading the file and append the control total number to the last byte.
def append_control_total(file_name, control_total):
    with open(file_name, 'ab') as f:
        f.write(control_total.to_bytes(8, byteorder='big'))


# 13. Compare two files
def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        if f1.read() == f2.read():
            print("The files are identical.")
        else:
            print("The files are different.")


# 14. Merge two files
def merge_files(file1, file2, dest_file):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2, open(dest_file, 'wb') as dest:
        dest.write(f1.read())
        dest.write(f2.read())


# 15. Determine the number of the specified byte
def count_byte(file_name, byte):
    with open(file_name, 'rb') as f:
        return f.read().count(byte)


# 16. Rename the file and set the date and time of file creation
def rename_file_with_datetime(file_name, new_file_name):
    os.rename(file_name, new_file_name)
    os.utime(new_file_name, None)


# 17. Rename the file, change its attributes
def rename_and_change_attributes(file_name, new_file_name, attributes):
    os.rename(file_name, new_file_name)
    os.chmod(new_file_name, attributes)
