

def get_game_results(line):
    # read game results from bballref csv
    try:
        date, bs, A, AS, H, HS, bl, ah = line.split(',')
    except:
        return {'winner':'None','loser':'None','date':'','score':'NA'}
                
    if int(AS) > int(HS):
        W, L = A, H
    else:
        W, L = H, A
    score = '%s-%s'%(AS,HS)
    return {'winner':W,'loser':L,'date':date,'score':score}

def update_loserbelt(gamelog, beltholder):
    if gamelog['winner'] == beltholder:
        beltholder = gamelog['loser']
        print '%s lost to %s on %s'%(gamelog['loser'],gamelog['winner'],gamelog['date'])
    return beltholder

def update_winnerbelt(gamelog, beltholder):
    if gamelog['loser'] == beltholder:
        beltholder = gamelog['winner']
        print '%s lost to %s on %s'%(gamelog['loser'],gamelog['winner'],gamelog['date'])
    return beltholder

def do_season(season_file, beltholder='New York Knicks', belt_type='loser'):
    year = season_file[5:9] # better save the seasons as YYYYetc
    with open(season_file,'r') as f:
        lines = f.readlines()[1:]
    for line in lines:
        game = get_game_results(line)
        if belt_type == 'loser':
            beltholder = update_loserbelt(game, beltholder)
        elif belt_type =='winner':
            beltholder = update_winnerbelt(game, beltholder)
        else:
            "print belt_type not recognized"
    print "################"
    print "END OF %s SEASON %s TITLE BELT HOLDER: %s"%(year,
                                                       belt_type.upper(),
                                                       beltholder)
    return beltholder

def do_history(start_year, belt_type='loser', beltholder='New York Knicks',
               end=2017):
    for year in range(start_year,end):
        beltholder = do_season('data/%s.csv'%year, 
                               belt_type=belt_type,beltholder=beltholder)

if __name__=="__main__":
    loser=0
    if loser:
        do_history(1947, end=1948, beltholder='New York Knicks')
        do_history(1948, end=1950, beltholder='Providence Steam Rollers')
        do_history(1950, end=1951, beltholder='St. Louis Bombers')
        do_history(1951, end=1952, beltholder='Minneapolis Lakers')
        do_history(1952, end=1955, beltholder='Fort Wayne Pistons')
        do_history(1955, end=1958, beltholder='Milwaukee Hawks')
        do_history(1958, end=1964, beltholder='St. Louis Hawks')
        do_history(1964, beltholder='New York Knicks')
        do_history(1979, end=1980, beltholder='Boston Celtics')
        do_history(1980, end=2013, beltholder='Utah Jazz')
        do_history(2013, beltholder='Brooklyn Nets')
    else:
        do_history(1947, end=1948, belt_type='winner', 
                   beltholder='Toronto Huskies')
        do_history(1948,belt_type='winner', beltholder='New York Knicks')
