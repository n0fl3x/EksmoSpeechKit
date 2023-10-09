import pytest

from file_to_text import file_to_text


GOOD_CASES = [
    (
        'test',
        {
            'raw_text': 'это тестовое аудио',
            'normalized_text': 'Это тестовое аудио.',
        },
    ),
    (
        'test-2',
        {
            'raw_text': 'шла маша по шоссе и сосала сушку',
            'normalized_text': 'Шла Маша по шоссе и сосала сушку.'
        },
    ),
]


@pytest.mark.parametrize('filename, exp_res', GOOD_CASES)
def test_file_to_text_good(filename, exp_res):
    assert file_to_text(filename=filename) == exp_res


BAD_CASES = [
    ('', None),
    (None, None),
    ([1, 2, 3], None),
]


@pytest.mark.parametrize('filename, exp_res', BAD_CASES)
def test_file_to_text_bad(filename, exp_res):
    assert file_to_text(filename=filename) == exp_res
