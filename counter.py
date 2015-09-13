# Sean Liu
# hw0 Script

def main():
    filename = 'iowa-liquor-sample.csv'
    matches = 0
    search = 'single malt scotch'

    f = open(filename, 'r')
    for record in f:
        if search in record.lower():
            matches += 1
    print 'Number of matches for ' + search + ':', matches

main()

