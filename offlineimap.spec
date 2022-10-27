Summary: Powerful IMAP/Maildir synchronization and reader support
Name: offlineimap
Version: 8.0.0
Release: 1
Source0: https://github.com/OfflineIMAP/offlineimap3/archive/refs/tags/v%{version}.tar.gz
License: GPL
Group: Networking/Mail
BuildArch: noarch
Url: http://www.complete.org/OldSoftwareSites
BuildRequires: python-devel
BuildRequires: python%{pyver}dist(imaplib2)
BuildRequires: python%{pyver}dist(rfc6555)
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
%autosetup -p1 -n offlineimap3-%{version}

%build
%py_build

%install
%py_install

%files
%doc COPY*
%doc offlineimap.conf*
%{_bindir}/offlineimap
%{py_puresitedir}/offlineimap
%{py_puresitedir}/*.egg-info
