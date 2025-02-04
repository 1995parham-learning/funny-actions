import argparse


def main():
    parser = argparse.ArgumentParser("issue")
    parser.add_argument("title", help="GitHub Issue Title", type=str)
    parser.add_argument("body", help="GitHub Issue Body", type=str)

    args = parser.parse_args()

    print(f"Thanks for creating an issue name {args.title}, we are working on it.")


if __name__ == "__main__":
    main()
