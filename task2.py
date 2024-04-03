import shelve


def save_links(link, links, filename):
    """Update links and save to file"""
    with shelve.open(filename) as file:
        links.update(link)
        file[filename] = links


def display_links(filename):
    """Display links from file"""
    try:
        with shelve.open(filename) as file:
            print(file[filename])
    except KeyError:
        print("No such file or directory")


if __name__ == "__main__":
    links_repo = {}

    link1, link_name1 = input("Enter link: ").strip(), input("Create link name: ")
    link2, link_name2 = input("Enter link: ").strip(), input("Create link name: ")
    link3, link_name3 = input("Enter link: ").strip(), input("Create link name: ")

    save_links({link1: link_name1}, links_repo, "links")
    save_links({link2: link_name2}, links_repo, "links")
    save_links({link3: link_name3}, links_repo, "links")

    display_links("links")
