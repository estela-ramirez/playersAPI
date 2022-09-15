import csv

# read csv, create & return players dict
def csv_to_json(csvFilePath):   
    players = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # makes each row a dict
        for rows in csvReader:
            # make playerID key
            key = rows['playerID']
            for k, v in rows.items():
                try:
                    rows[k] = int(v)
                except ValueError:
                    pass
            players[key] = rows
 
    return players