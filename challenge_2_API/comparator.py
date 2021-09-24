from src.response_comparator import ResponseComparator

file1_path = r"challenge_2_API\data\file1.txt"
file2_path = r"challenge_2_API\data\file2.txt"

if __name__ == '__main__':

    with open(file1_path, "r") as file1:
        for url1 in file1:
            with open(file2_path, "r") as file2:
                for url2 in file2:
                    response_comparator = ResponseComparator(url1, url2)
                    try:
                        response_comparator.print_output()
                    except:
                        continue
                    print('')
                    




