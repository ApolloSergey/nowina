import logging


class Verify(object):
    @staticmethod
    def equals(expected, actual, message_on_fail):
        try:
            assert expected == actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error("%s: %s", err_type, message_on_fail)
            logging.debug("\n\texpected: %s  \n\tactual:   %s", expected, actual)
            raise err

    @staticmethod
    def not_equals(expected, actual, message_on_fail):
        try:
            assert expected is not actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error("%s: %s", err_type, message_on_fail)
            logging.debug("%s should not be equal to %s", expected, actual)
            raise err

    @staticmethod
    def true(condition, message_on_fail):
        try:
            assert condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error("%s: %s", err_type, message_on_fail)
            raise err

    @staticmethod
    def false(condition, message_on_fail):
        try:
            assert not condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error("%s: %s", err_type, message_on_fail)
            raise err
