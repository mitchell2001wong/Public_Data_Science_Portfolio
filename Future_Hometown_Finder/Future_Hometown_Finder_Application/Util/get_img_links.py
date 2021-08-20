from apiclient.discovery import build # ignore this warning

api_key = "AIzaSyD0efTquIAOAZH3oCI4WDZdLr8c01cHUHA"
resource = build("customsearch", 'v1', developerKey=api_key).cse()

def get_img_links(city, state):
    """
    city: string
        The name of the city.
    state: string
        The name of the state.
    
    return: a list of links to images as strings
    """
    result = resource.list(q=city + state, cx="ebc5f83c42b62df9d", searchType="image",).execute()
    return [item["link"] for item in result['items']]