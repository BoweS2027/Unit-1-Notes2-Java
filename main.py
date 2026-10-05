# lists - a data collection option that is ordered and mutable
def main():
    my_list = []
    my_other_list = list()
    my_classes = ["math", "computer science", "english"]
    print (len(my_classes))
    print(my_classes[2])
    print(my_classes[len(my_classes)-1])
    print(my_classes[-1])
    my_classes[1] = "ap"
    print(my_classes)
    my_classes[1] += " comp sci"
    print(my_classes)


if __name__ == "__main__":
    main()
