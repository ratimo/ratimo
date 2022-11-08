def get_eps_mean(name):
    try:
        #print(Ticker(name).key_stats.get(name).get('forwardEps'))#TÄMÄ TAPA TOIMII JEEE
        stonk1=Ticker(name).income_statement()
        stonk1=stonk1[['asOfDate','BasicEPS']].dropna()
        kurssi=Ticker(name).financial_data.get(name).get('currentPrice')
        eps_mean=stonk1['BasicEPS'].mean()
        gpe=kurssi/eps_mean
        havainnot=stonk1['BasicEPS'].count()
        #print(f'Osakekurssi / EPS({havainnot}v. keskiarvo): {gpe:.2f}')
        return gpe
    except KeyError:
        print('-')
def get_eps_base_years(name):
    havainnot=stonk1['BasicEPS'].count()
    return havainnot

def get_industry(name):
    industry = Ticker(name).summary_profile[name]["industry"]
    return industry
    
def get_country(name):
    country = Ticker(name).summary_profile[name]["country"]
    return country
    
def get_name(name):
    company_name = Ticker(name).quote_type[name]["longName"]
    return company_name
    
def get_earnings_report(name):
    return Ticker(f'{name}').get_modules('earnings')

def get_stonks_count(name):
    try:
        stonks=Ticker(name).get_financial_data('ShareIssued').query('asOfDate == asOfDate.max()')
        stonks=int(stonks['ShareIssued'])
        #print("Total stonks",stonks)  
        return stonks
    except KeyError:
        print('-')
def get_revenue(name):
    revenue=Ticker(name).get_financial_data('totalRevenue')
    return revenue

def get_equity(name):
    types = ['TotalEquityGrossMinorityInterest','ShareIssued']
    stonk2=Ticker(name).get_financial_data(types)
    stonk2=stonk2.query('asOfDate == asOfDate.max()')
    bookvalue=int(stonk2['TotalEquityGrossMinorityInterest'])
    return bookvalue
