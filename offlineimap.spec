Summary: Powerful IMAP/Maildir synchronization and reader support
Name: offlineimap
Version: 6.5.3.1
Release: 1
Source0: https://github.com/downloads/spaetz/offlineimap/offlineimap-%{version}.tar.gz
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
%setup -q -n spaetz-%{name}-ebd5fe2/

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc COPY*
%doc offlineimap.conf*
%{_bindir}/offlineimap
%{py_puresitedir}/offlineimap
%{py_puresitedir}/*.egg-info


%changelog
* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.5.3.1-1
+ Revision: 794260
- version update 6.5.3.1

* Tue Jan 17 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.5.2-1
+ Revision: 761969
- version update 6.5.2

* Mon Jan 09 2012 Alexander Khrukin <akhrukin@mandriva.org> 6.5.1.2-1
+ Revision: 759220
- version update 6.5.1.2

* Wed Nov 23 2011 Alexander Khrukin <akhrukin@mandriva.org> 6.4.0-1
+ Revision: 732996
- version bump 6.4.0

* Mon Nov 08 2010 Jérôme Quelin <jquelin@mandriva.org> 6.2.0-5mdv2011.0
+ Revision: 595108
- rebuild for new python

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 6.2.0-4mdv2011.0
+ Revision: 590159
- rebuild for python 2.7

* Thu Aug 13 2009 Frederik Himpe <fhimpe@mandriva.org> 6.2.0-3mdv2010.0
+ Revision: 416206
- Update to new version 6.2.0

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 4.0.15-3mdv2009.1
+ Revision: 325774
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 4.0.15-2mdv2008.1
+ Revision: 136634
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

