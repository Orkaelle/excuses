import csv


RAW_CSV_PATH = './DATAS/RAW/A2019_12.csv'
CURATED_LOCAL_PATH = './DATAS/CURATED/'

def split_data(FILE_PATH, COLUMN):
    '''
    Break raw data into many files
    '''
    
    print ('Spliting csv...')
    with open(FILE_PATH, encoding='utf-8') as file_stream:  
        csv.field_size_limit(10000000)  
        file_stream_reader = csv.DictReader(file_stream, delimiter=';')

        open_files_references = {}

        for row in file_stream_reader:
            column = row[COLUMN]
     
            # Open a new file and write the header
            if column not in open_files_references:
                output_file = open(CURATED_LOCAL_PATH + f'{column}.csv', 'w', encoding='utf-8', newline='')
                dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                dictionary_writer.writeheader()
                open_files_references[column] = output_file, dictionary_writer
            # Always write the row
            open_files_references[column][1].writerow(row)
        # Close all the files
        for output_file, _ in open_files_references.values():
            output_file.close()
    
    print ('Done.')


split_data(RAW_CSV_PATH,'AGE_BEN_SNDS')