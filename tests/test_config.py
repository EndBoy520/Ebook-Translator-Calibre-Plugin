import unittest
import calibre_plugins.ebook_translator.config as config


class TestConfig(unittest.TestCase):

    def test_init_config(self):
        default = {
            'to_library': True,
            'output_path': None,
            'translate_engine': 'Google',
            'api_key': {},
            'proxy_enabled': False,
            'proxy_setting': [],
            'request_attempt': 3,
            'request_interval': 5,
            'cache_enabled': True,
            'log_translation': True,
            'translation_position': 'after',
            'rule_mode': 'normal',
            'filter_rules': [],
        }
        config.preferences = None

    def test_set_and_get_config(self):
        config.preferences = {
            'a': 1,
            'b': {
                'b1': 2,
                'b2': True,
                'b3': False,
            }
        }

        self.assertIsNone(config.get_config('a.fake'))
        self.assertEqual(1, config.get_config('a.fake', 1))

        self.assertTrue(config.get_config('b.b2'))
        self.assertFalse(config.get_config('b.b3'))

        config.set_config('a.a1', 1)

        self.assertEqual(1, config.preferences['a']['a1'])
        self.assertEqual(1, config.get_config('a.a1'))

        config.set_config('b', 2)

        self.assertEqual(2, config.preferences['b'])
        self.assertEqual(2, config.get_config('b'))

        config.set_config('c', 3)

        self.assertEqual(3, config.preferences['c'])
        self.assertEqual(3, config.get_config('c'))

        config.set_config('d.d1.d11.d111', 4)

        self.assertEqual(4, config.preferences['d']['d1']['d11']['d111'])
        self.assertEqual(4, config.get_config('d.d1.d11.d111'))

        self.assertEqual(config.preferences, {
            'a': {
                'a1': 1
            },
            'b': 2,
            'c': 3,
            'd': {
                'd1': {
                    'd11': {
                        'd111': 4
                    }
                }
            }
        })

    def test_save_config(self):
        config.preferences = {'a': 1, 'b': 2}
        config.save_config({'a': 3, 'b': 4, 'c': 5})

        self.assertEqual({'a': 3, 'b': 4, 'c': 5}, config.preferences)

    def test_get_configs(self):
        config.preferences = {'a': 1, 'b': 2}

        self.assertEqual([1, 2], config.get_configs('a', 'b'))
