import os
import tqdm
import lzma

def xz_files_in_dir(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith('.xz')]
    
folder_path = "/Users/zuzannajezierska/Desktop/fcc-llm-course/xz_files"
output_file = "output_{}.txt"
vocab_file = "vocab.txt"
split_files = int(input("Enter number of files to split into: "))

files = xz_files_in_dir(folder_path)
total_files = len(files)

max_count = total_files // split_files if split_files != 0 else total_files

vocab = set()

# Splitting the files and extracting text
for i in range(split_files):
    with open(output_file.format(i), 'w', encoding='utf-8') as outfile:
        for count, filename in enumerate(tqdm(files[:max_count], total=max_count)):
            if count >= max_count:
                break
            file_path = os.path.join(folder_path, filename)
            with lzma.open(file_path, 'rt', encoding='utf-8') as infile:
                text = infile.read()
                outfile.write(text)
                characters = set(text)
                vocab.update(characters)
        files = files[max_count:]    

    # Writing the vocabulary to a file
    with open(vocab_file, 'w', encoding='utf-8') as vfile:
        for char in vocab:
            vfile.write(char + '\n')