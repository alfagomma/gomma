
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Base test
"""

import logging

from gomma.base.core import Base


class test():
    """ Test base """

    def __init__(self, profile_name=None):
        """init"""
        logging.debug(f'Init test {profile_name}')
        self.b = Base(profile_name)

 

def main(args):
    """ start testing """
    logging.basicConfig(level=logging.INFO)
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    logging.debug(f'Init {__file__}')
    b = Base(profile_name=args.profile)
    # users = b.listUser({'domain':2, 'active': True})
    # print(users)
    # u = b.getUser(2443)
    # print(u)
    # nl = b.listIntnewsletter()
    # n = b.getIntnewsletter(12, {'include':'flashnews'})
    # print(n)
    return


def parse_args():
    """Parse the args from main."""
    import argparse
    parser = argparse.ArgumentParser(description='Testing support')
    parser.add_argument("--profile", type=str, help='Use specific profile env')
    # parser.add_argument("-t", "--test", nargs='+',
    #                     help='What can I do for you?', required=True)
    parser.add_argument("-v", "--verbose",
                        help="increase output verbosity", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)
