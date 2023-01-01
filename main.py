from httpx import get, post
import base64
#
#
#
#
def image_from_media(img_src):
    """This functions will return (image from folder) codes into Gutenberg format for WordPress post.
    input: You have to input (image source from folder)"""
    media_url = f'https://localhost/demosite/wp-json/wp/v2/media' # change the website address
    files = {'file': open(img_src, 'rb')}
    return files

def headers(wp_user, wp_pass):
    """This functions will return (wp headers) for WordPress.
    input: You have to input (username & password)"""
    import base64
    wp_credential = f'{wp_user}:{wp_pass}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
    return wp_header

keyword = 'birds'
api_key = 'PIXABAY_API_KEY'  # put your pixabay API key here
pixabay_api = f'https://pixabay.com/api/?key={api_key}&q={keyword}&image_type=photo'
img_url = get(pixabay_api).json().get('hits')[0].get('largeImageURL')

# ## image download and uploading ##
res = get(f'{img_url}')
with open(f'{keyword}.jpg', 'wb') as file:
    file.write(res.content)
    features_img = image_from_media(f'{keyword}.jpg')


# uploading to WordPress
header = headers('wp_user', 'wp_pass')

media_upload_json = 'https://localhost/demosite/wp-json/wp/v2/media' # change the website address
res_id = post(media_upload_json, files=features_img, headers=header, verify=False)
feature_img_id = res_id.json().get('id')

print('congrats, your feature img id is: ', feature_img_id)

# end of image download and uploading #
