%define name offlineimap
%define version 4.0.15
%define rel 2

Summary: Powerful IMAP/Maildir synchronization and reader support
Name: %{name}
Version: %{version}
Release: %mkrel %{rel}
Source: http://www.quux.org/devel/offlineimap/%{name}_%{version}.tar.bz2
License: GPL
Group: Networking/Mail
Prefix: %{_prefix}
BuildArch: noarch
Url: http://www.quux.org/devel/offlineimap
Buildrequires: python-devel >= %{pyver} gzip
Requires: python >= %{pyver}

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
%setup -q -n %{name}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp offlineimap.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc UPGRADING README COPYRIGHT 
%doc offlineimap.conf*
%doc manual.*
%{_bindir}/offlineimap
%{py_puresitedir}/offlineimap
%{py_puresitedir}/*.egg-info
%{_mandir}/man1/offlineimap.1*


