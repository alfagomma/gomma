
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ELEMENT test
"""

import logging

from gomma.element.core import Element


class test():
    """test element"""

    def __init__(self, profile_name):
        """ init """
        logging.debug(f'Init test {profile_name}')
        self.h = Element(profile_name)

    def item(self):
        """test item"""
        try:
            r = self.h.attachItemErp(7, {'erp_id': 1, 'code': '2307324'})
        except Exception as e:
            print(e)
            return False
        print(r)
        return True


def main(args):
    """ start testing """
    logging.basicConfig(level=logging.INFO)
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(f'Init {__file__}')
    t = test(profile_name=args.profile)
    for atr in args.test:
        if hasattr(t, atr):
            getattr(t, atr)()
    return


def parse_args():
    """Parse the args from main."""
    import argparse
    parser = argparse.ArgumentParser(description='Testing support')
    parser.add_argument("--profile", type=str, help='Use specific profile env')
    parser.add_argument("-t", "--test", nargs='+',
                        help='What can I do for you?', required=True)
    parser.add_argument("-v", "--verbose",
                        help="increase output verbosity", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)
