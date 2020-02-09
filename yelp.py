from yelpapi import YelpAPI
yelp_api = YelpAPI('9pdRr_PCd8m5NcXB6bb6cdRmKgeXzz-TUrQfdn8lCZrdEVFqMa3YSygop0Mnp-xKUjTzBZv5VsGh3mW8bE_dM5d24Y7u0cDhKMNG40AqRUTYjc1PSlXaWA1ce9UsXXYx')

response = yelp_api.search_query(term='olive garden', location='san jose', limit='5')

print(yelp_api.reviews_query(id="kyCAxIcS_axZB12EtHV1FA"))
