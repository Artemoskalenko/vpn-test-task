def link_replacement_function(url, site_name, soup):
    protocols = ('http://', 'https://')

    # changing 'href' link
    for tag in soup.find_all(['img', 'script', 'link', 'use'], href=True):
        href = tag.get('href')
        if not href.startswith(protocols):
            tag['href'] = url + href

    # changing 'src' link
    for tag in soup.find_all(['img', 'script', 'link', 'use'], src=True):
        src = tag.get('src')
        if not src.startswith(protocols):
            tag['src'] = url + src

    # changing 'form' link
    for tag in soup.find_all(['form'], action=True):
        action = tag.get('action')
        if not action.startswith(protocols):
            tag['action'] = url + action

    # changing 'srcset' link
    for tag in soup.find_all(['img', 'script', 'link', 'use'], attrs={'srcset': True}):
        srcset_of_element = tag["srcset"].split(", ")
        for index, srcset in enumerate(srcset_of_element):
            if not srcset.startswith(protocols):
                srcset_of_element[index] = url + srcset
        tag['srcset'] = ', '.join(srcset_of_element)

    # changing 'href' link for 'a' tag
    for tag in soup.find_all('a', href=True):
        href = tag.get('href')
        if not href.startswith(protocols):
            tag['href'] = f'/{site_name}{href}'
        elif href.startswith(url):
            tag['href'] = href.replace(url, f'/{site_name}')

    return soup


def serialize_headers(headers):
    """HTTP headers as a bytestring."""
    return b"\r\n".join(
        [
            key.encode("ascii") + b": " + value.encode("latin-1")
            for key, value in headers.items()
        ]
    )


def serialize(request):
    """Full HTTP message, including headers, as a bytestring."""
    return serialize_headers(request.headers) + b"\r\n\r\n" + request.body