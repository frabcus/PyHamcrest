from hamcrest.core.base_matcher import BaseMatcher

__author__ = "Jon Reid"
__copyright__ = "Copyright 2011 hamcrest.org"
__license__ = "BSD, see License.txt"


class IsEqualIgnoringCase(BaseMatcher):

    def __init__(self, string):
        if not isinstance(string, basestring):
            raise TypeError('IsEqualIgnoringCase requires string')
        self.original_string = string
        self.lowered_string = string.lower()

    def _matches(self, item):
        if not isinstance(item, basestring):
            return False
        return self.lowered_string == item.lower()

    def describe_to(self, description):
        description.append_description_of(self.original_string)    \
                   .append_text(' ignoring case')


def equal_to_ignoring_case(string):
    """Matches if object is a string equal to a given string, ignoring case
    differences.

    :param string: The string to compare against as the expected value.

    This matcher first checks whether the evaluated object is a string. If so,
    it compares it with ``string``, ignoring differences of case.

    Example::

        equal_to_ignoring_case("hello world")

    will match "heLLo WorlD".

    """
    return IsEqualIgnoringCase(string)
