import shelve


def add_link(links):
    """Add link and link alias to the dict"""
    link, link_name = input("Enter link: ").strip(), input("Create link name: ")
    links.update({link: link_name})


def save_links(links, filename):
    """Save links to file"""
    shelve_file = shelve.open(filename)
    shelve_file[filename] = links


def display_links(filename):
    """Display links from file"""
    try:
        shelve_links = shelve.open(filename)
        links = shelve_links[filename]
        print(links)
    except KeyError:
        print("No such file or directory")


if __name__ == "__main__":
    links_repo = {}
    add_link(links_repo)
    add_link(links_repo)
    add_link(links_repo)

    save_links(links_repo, "links")
    display_links("links")
