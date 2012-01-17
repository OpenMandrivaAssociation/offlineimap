Summary: Powerful IMAP/Maildir synchronization and reader support
Name: offlineimap
Version: 6.5.2
Release: 1
Source0: https://github.com/downloads/spaetz/offlineimap/offlineimap-v%{version}.tar.gz
License: GPL
Group: Networking/Mail
Prefix: %{_prefix}
BuildArch: noarch
Url: http://www.complete.org/OldSoftwareSites
Buildrequires: python-devel
Requires: python 

%description
OfflineIMAP is a tool to simplify your e-mail  reading.  With
OfflineIMAP, you can read the same mailbox from multiple computers.
You get a current copy of your messages on each computer, and changes
you make one place will be visible on all other systems. For instance,
you can delete a message on your home computer, and it will appear
deleted on your work computer as well. OfflineIMAP is also useful if
you want to use a mail reader that does not have IMAP support, has poor
IMAP support, or does not provide disconnected operation.

%prep
%setup -q -n spaetz-%{name}-091272d

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc COPY*
%doc offlineimap.conf*
%{_bindir}/offlineimap
%{py_puresitedir}/offlineimap
%{py_puresitedir}/*.egg-info
