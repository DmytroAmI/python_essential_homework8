import shelve


def create_shelve_links(links, filename):
    """Create shelve and add links to file"""
    with shelve.open(filename) as shelf:
        shelf["links"] = links


def add_link_to_shelve(link, filename):
    """Update shelve, add link to file"""
    with shelve.open(filename) as shelf:
        data = shelf["links"]
        data.update(link)
        shelf["links"] = data


def display_links(filename):
    """Display links from file"""
    try:
        with shelve.open(filename) as shelf:
            print(shelf["links"])
    except KeyError:
        print("No such file or directory")


def input_link():
    """Input link and link alias"""
    link = input("Enter the link: ").strip()
    link_alias = input("Create a new link alias: ").strip()
    return {link: link_alias}


if __name__ == "__main__":
    create_shelve_links({}, "links_repository.dat")

    add_link_to_shelve(input_link(), "links_repository.dat")
    add_link_to_shelve(input_link(), "links_repository.dat")
    add_link_to_shelve(input_link(), "links_repository.dat")

    display_links("links_repository.dat")
