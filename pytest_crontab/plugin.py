

def pytest_addoption(parser):
    parser.addoption('--crontab', help='register contab tasks')
    parser.addoption('--crontab-user', help='contab tasks user')


def pytest_cmdline_main(config):
    crontab = config.getoption('--crontab')
    user = config.getoption('--crontab-user') or 'root'
    if crontab:
        crontab_file = f'/var/spool/cron/{user}'

        with open(crontab_file, 'a', encoding='utf-8') as f:
            f.write(f'\n{crontab} cd {config.rootdir}; pytest . >>pytest.log\n')
        return True
