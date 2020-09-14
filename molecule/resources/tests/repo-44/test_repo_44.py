
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_repo_file(host):
    f = None
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/etc/apt/sources.list.d/powerdns-rec-44.list')
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/etc/yum.repos.d/powerdns-rec-44.repo')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_pdns_repo(host):
    f = None
    if host.system_info.distribution.lower() in debian_os:
        f = host.file('/etc/apt/sources.list.d/powerdns-rec-44.list')
    if host.system_info.distribution.lower() in rhel_os:
        f = host.file('/etc/yum.repos.d/powerdns-rec-44.repo')

    assert f.exists
    assert f.contains('rec-44')


def test_pdns_version(host):
    cmd = host.run('/usr/sbin/pdns_recursor --version')

    assert 'PowerDNS Recursor' in cmd.stderr
    assert '4.4' in cmd.stderr
