
%define		_ver		1.0.1

Summary:	K Desktop Environment - network applications
Summary(es.UTF-8):	K Desktop Environment - aplicaciones de red
Summary(pl.UTF-8):	K Desktop Environment - aplikacje sieciowe
Summary(pt_BR.UTF-8):	K Desktop Environment - aplicações de rede
Name:		kdenetwork-kroupware
Version:	%{_ver}
Release:	3
License:	GPL
Group:		X11/Libraries
Source0:	http://www.erfrakon.de/projects/kolab/download/kde-kolab-client-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	a250b51c787e5d18ca18bdad660b6b67
Source2:	lisa.init
Source3:	lisa.sysconfig
Source4:	kdenetwork-lisarc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.1.1
BuildRequires:	libtool
BuildRequires:	libxml2-progs
BuildRequires:	perl
BuildRequires:	qt-devel >= 6:3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Provides:	kdenetwork
Obsoletes:	kdenetwork
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE network applications. Package includes:
- KDict - Online dictionary client
- KGet - file downloader
- KIT - AOL Instant Messenger
- KMail - e-mail client. Patched for proper charsets support
- KNewsticker - News Ticker
- KNODE - news client
- KORN - "biff" program
- KPF - Public fileserver applet
- KPPP - PPP dialer
- KRFB - virtual desktops
- KSirc - IRC client
- KTalkd - takt daemon
- KXmlRpcd - XmlRpc Daemon
- Lanbrowser - LAN Browser

%description -l pl.UTF-8
Aplikacje sieciowe KDE. Pakiet zawiera:
- KDict - klient słownika
- KGet - ściągacz plików
- KIT - klient AOL Instant Messenger
- KMail - program pocztowy, z poprawioną obsługą zestawów znaków
- KORN - program pokazujący stan skrzynek pocztowych
- KPF - applet publicznego serwera plików
- KPPP - program do nawiązywania połączeń modemowych
- KNewsticker - News Ticker
- KNODE - program do czytania newsów
- KRFB - wirtualne biurka
- KSirc - klient IRC
- KTalkd - demon Talk
- KXmlRpcd - demon XmlRpc
- Lanbrowser - przeglądarka LAN-u

%description -l pt_BR.UTF-8
Aplicações de Rede para o KDE.

Incluídos neste pacote:

kmail: leitor de correio knu: utilitários de rede korn: ferramenta de
monitoração da caixa de correio kppp: configuração fácil para conexão
PPP krn: leitor de notícias

%package devel
Summary:	Header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja developerska
Summary(pt_BR.UTF-8):	Arquivos de inclusão para compilar aplicações que usem as bibliotecas do kdenetwork
Group:		X11/Development/Libraries
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-devel
Obsoletes:	kdenetwork-devel

%description devel
Header files and development documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja developerska.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para compilar aplicações que usem as bibliotecas
do kdenetwork.

%package kdict
Summary:	Online dictionary client
Summary(pl.UTF-8):	Klient słownika
License:	Artistic
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-kdict
Provides:	kdict
Obsoletes:	kdenetwork-kdict
Obsoletes:	kdict

%description kdict
Online dictionary client.

%description kdict -l pl.UTF-8
Klient słownika.

%description kdict -l pt_BR.UTF-8
kdict é um utilitário de dicionário que usa servidores dictd da
Internet.

%package kinetd
Summary:	KDE Internet Daemon
Summary(pl.UTF-8):	Demon internetowy KDE
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-kinetd
Obsoletes:	%{name}-krfb < 3.1-6
Obsoletes:	kdenetwork-kinetd

%description kinetd
An Internet daemon that starts network services on demand.

%description kinetd -l pl.UTF-8
Demon internetowy, który uruchamia na żądanie usługi sieciowe.

%package kget
Summary:	File Downloander
Summary(pl.UTF-8):	Ściągacz plików
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-kget
Obsoletes:	kdenetwork-kget

%description kget
File Downloader.

%description kget -l pl.UTF-8
Ściągacz plików.

%package kit
Summary:	KDE AOL Instant Messenger
Summary(pl.UTF-8):	Klient AOL Instant Messenger dla KDE
Summary(pt_BR.UTF-8):	Comunicador que usa o protocolo AOL
License:	LGPL
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-kit
Obsoletes:	kdenetwork-kit

%description kit
KDE AOL Instant Messenger.

%description kit -l pl.UTF-8
Klient AOL Instant Messenger dla KDE.

%description kit -l pt_BR.UTF-8
Comunicador que usa o protocolo AOL.

%package kmail
Summary:	KDE Mail client
Summary(pl.UTF-8):	Program pocztowy KDE
Summary(pt_BR.UTF-8):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
Requires:	%{name} >= %{version}
Requires:	kdebase-mailnews
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-kmail
Obsoletes:	kdenetwork-kmail

%description kmail
This is electronic mail client for KDE. It is able to retrievie mail
from POP3 accounts and from local mailboxes.

This package contains version patched for better charset support.

%description kmail -l pl.UTF-8
Program pocztowy dla KDE. Potrafi odczytywać pocztę z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersją programu z poprawioną obsługą zestawów
znaków.

%description kmail -l pt_BR.UTF-8
Poderoso cliente / leitor de e-mails para o KDE.

%package knewsticker
Summary:	KDE News Ticker
Summary(pl.UTF-8):	News Ticker dla KDE
Summary(pt_BR.UTF-8):	Miniaplicativo de exibição de notícias para o painel Kicker
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-knewsticker
Obsoletes:	kdenetwork-knewsticker

%description knewsticker
KDE News Ticker.

%description knewsticker -l pl.UTF-8
News Ticker dla KDE.

%description knewsticker -l pt_BR.UTF-8
Miniaplicativo de exibição de notícias para o painel Kicker.

%package knode
Summary:	KDE News Reader
Summary(pl.UTF-8):	Czytnik newsów dla KDE
Summary(pt_BR.UTF-8):	Leitor de notícias (news) do KDE
Group:		X11/Applications
Requires:	%{name} >= %{version}
Requires:	kdebase-mailnews
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-knode
Obsoletes:	kdenetwork-knode

%description knode
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description knode -l pl.UTF-8
Czytnik newsów dla KDE. Obsługuje wątki oraz killfile.

%description knode -l pt_BR.UTF-8
Leitor de notícias (news) do KDE.

%package korn
Summary:	KDE 'biff' application
Summary(pl.UTF-8):	Wskaźnik skrzynki pocztowej dla KDE
Summary(pt_BR.UTF-8):	Miniaplicativo de monitoração da caixa de correio
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-korn
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl.UTF-8
Programik pokazujący ilość wiadomości w wybranych folderach
pocztowych.

%description korn -l pt_BR.UTF-8
Miniaplicativo de monitoração da caixa de correio.

%package kpf
Summary:	Public fileserver applet
Summary(pl.UTF-8):	Applet publicznego serwera plików
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-kpf
Obsoletes:	kdenetwork-kpf

%description kpf
Public fileserver applet.

%description kpf -l pl.UTF-8
Applet publicznego serwera plików.

%package kppp
Summary:	KDE PPP dialer
Summary(pl.UTF-8):	Program do połączeń modemowych dla KDE
Summary(pt_BR.UTF-8):	O discador para Internet
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Requires:	ppp
Provides:	kdenetwork-kppp
Obsoletes:	kdenetwork-kppp

%description kppp
A PPPP dialer for KDE. It supports multiple accounts.

%description kppp -l pl.UTF-8
Program no nawiązywania połączeń modemowych pod KDE. Posiada łatwy
interfejs i możliwość zdefiniowania kilku kont.

%description kppp -l pt_BR.UTF-8
O discador para Internet.

%package ksirc
Summary:	KDE IRC client
Summary(pl.UTF-8):	Klient IRC dla KDE
Summary(pt_BR.UTF-8):	Cliente de IRC do KDE
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-ksirc
Obsoletes:	kdenetwork-ksirc

%description ksirc
KDE IRC client.

%description ksirc -l pl.UTF-8
Klient IRC dla KDE.

%description ksirc -l pt_BR.UTF-8
Cliente de IRC do KDE.

%package krfb
Summary:	Virtual Desktops
Summary(pl.UTF-8):	Wirtualne biurka
Group:		X11/Applications
Requires:	%{name}-kinetd = %{version}
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-krfb
Obsoletes:	kdenetwork-krfb

%description krfb
Virtual Desktops.

%description krfb -l pl.UTF-8
Wirtualne biurka.

%package ktalkd
Summary:	Talk daemon
Summary(pl.UTF-8):	Daemon talk
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-ktalkd
Obsoletes:	kdenetwork-ktalkd

%description ktalkd
Talk daemon.

%description ktalkd -l pl.UTF-8
Demon talk.

%package ktnef
Summary:	A viewer/extractor for TNEF files
Summary(pl.UTF-8):	Konwerter/ekstraktor plików TNEF
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-ktnef
Obsoletes:	kdenetwork-ktnef

%description ktnef
A viewer/extractor for TNEF files.

%description ktnef -l pl.UTF-8
Konwerter/ekstraktor plików TNEF.

%package kxmlrpcd
Summary:	KDE XmlRpc Daemon
Summary(pl.UTF-8):	Deamon XmlRpc dla KDE
Group:		X11/Applications
Requires:	kdelibs >= 3.1.1
Provides:	kdenetwork-kxmlrpcd
Obsoletes:	kdenetwork-kxmlrpcd

%description kxmlrpcd
KDE XmlRpc Daemon.

%description kxmlrpcd -l pl.UTF-8
Demon XmlRpc dla KDE.

%package lanbrowser
Summary:	KDE LAN Browser
Summary(pl.UTF-8):	Przeglądarka LAN-u dla KDE
Group:		X11/Applications
Requires:	rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	konqueror >= 3.1.1
Obsoletes:	%{name}-lisa
Obsoletes:	lisa
Provides:	lisa
Provides:	kdenetwork-lanbrowser
Obsoletes:	kdenetwork-lanbrowser

%description lanbrowser
KDE LAN Browser.

%description lanbrowser -l pl.UTF-8
Przeglądarka LAN-u dla KDE.

%prep
%setup -q

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_cv_utmp_file=/var/run/utmpx ; export kde_cv_utmp_file

#%{__aclocal}
#%{__autoconf}
#%{__automake}
%configure2_13 \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-kernel-threads \
	--with-pam="yes" \
	--disable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_datadir}/applnk -name '*.desktop'` ; then
	mv $f $RPM_BUILD_ROOT%{_desktopdir}/kde

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/lisa
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/lisa
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/lisarc

cd $RPM_BUILD_ROOT%{_pixmapsdir}
mv {locolor,crystalsvg}/16x16/apps/krfb.png
cd -

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post lanbrowser
/sbin/chkconfig --add lisa
if [ -r /var/lock/subsys/lisa ]; then
	/etc/rc.d/init.d/lisa restart >&2
else
	echo "Run \"/etc/rc.d/init.d/lisa start\" to start Lisa daemon."
fi

%preun lanbrowser
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/lisa ]; then
		/etc/rc.d/init.d/lisa stop >&2
	fi
	/sbin/chkconfig --del lisa
fi

%files
%defattr(644,root,root,755)
%{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*
%{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*.*
%{_libdir}/kde3/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so*
%{_datadir}/services/sieve.protocol

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmimelib.so
%attr(755,root,root) %{_libdir}/libkdenetwork.so
%{_includedir}/*

%files kdict
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdict
%{_libdir}/kde3/kdict_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kdict_panelapplet.so
%{_datadir}/apps/kdict
%{_datadir}/apps/kicker/applets/kdictapplet.desktop
%{_iconsdir}/*/*/*/kdict*
%{_desktopdir}/kde/kdict.desktop

%files kget
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kget
%{_libdir}/kde3/khtml_kget.la
%attr(755,root,root) %{_libdir}/kde3/khtml_kget.so
%{_datadir}/apps/kget
%{_datadir}/apps/khtml/kpartplugins/kget_plug_in.rc
%{_datadir}/mimelnk/application/x-kgetlist.desktop
%{_iconsdir}/*/*/*/*kget*
%{_desktopdir}/kde/kget.desktop

%files kinetd
%defattr(644,root,root,755)
%{_libdir}/kde3/kded_kinetd.la
%attr(755,root,root) %{_libdir}/kde3/kded_kinetd.so
%{_datadir}/apps/kinetd
%{_datadir}/services/kded/kinetd.desktop
%{_datadir}/servicetypes/kinetdmodule.desktop

%files kit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kit
%{_datadir}/apps/kit
%{_desktopdir}/kde/kit.desktop
%{_iconsdir}/*/*/*/kit.png

%files kmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%attr(755,root,root) %{_bindir}/kgpgcertmanager
%attr(755,root,root) %{_bindir}/mail.local
%{_libdir}/kde3/kfile_rfc822.la
%attr(755,root,root) %{_libdir}/kde3/kfile_rfc822.so
%{_datadir}/apps/kconf_update/k[!n]*
%{_datadir}/apps/kconf_update/u*
%{_datadir}/apps/kgpgcertmanager/kgpgcertmanagerui.rc
%{_datadir}/apps/kmail
%{_datadir}/services/kfile_rfc822.desktop
%{_desktopdir}/kde/KMail.desktop
%{_desktopdir}/kde/kmailcvt.desktop
%{_iconsdir}/*/*/*/kmail*.png

%files knewsticker
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knewstickerstub
%{_libdir}/kde3/knewsticker_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/knewsticker_panelapplet.so
%{_libdir}/kde3/kcm_knewsticker.la
%attr(755,root,root) %{_libdir}/kde3/kcm_knewsticker.so
%{_desktopdir}/kde/kcmnewsticker.desktop
%{_desktopdir}/kde/knewsticker*.desktop
%{_datadir}/applnk/.hidden/knewstickerstub.desktop
%{_datadir}/applnk/.hidden/kcmnewsticker.desktop
%{_datadir}/services/knewsservice.protocol
%{_datadir}/apps/knewsticker
%{_datadir}/apps/kicker/applets/knewsticker.desktop
%{_datadir}/apps/kconf_update/kn*
%{_iconsdir}/*/*/*/knewsticker.png

%files knode
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_desktopdir}/kde/KNode.desktop
%{_datadir}/apps/knode
%{_iconsdir}/*/*/*/knode.png

%files korn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png

%files kpf
%defattr(644,root,root,755)
%{_libdir}/kde3/kpf_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kpf_panelapplet.so
%{_libdir}/kde3/kpfpropertiesdialog.la
%attr(755,root,root) %{_libdir}/kde3/kpfpropertiesdialog.so
%{_datadir}/apps/kicker/applets/kpf*
%{_datadir}/services/kpfpropertiesdialogplugin.desktop
%{_iconsdir}/*/*/*/kpf*

%files kppp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_desktopdir}/kde/Kppp.desktop
%{_desktopdir}/kde/kppplogview.desktop
%{_datadir}/apps/kppp
%{_iconsdir}/*/*/*/kppp.png

%files krfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krdc
%attr(755,root,root) %{_bindir}/krfb
%{_libdir}/kde3/kcm_krfb.la
%attr(755,root,root) %{_libdir}/kde3/kcm_krfb.so
%{_datadir}/apps/krdc
%{_datadir}/apps/krfb
%{_datadir}/services/kinetd_krfb.desktop
%{_datadir}/services/vnc.protocol
%{_desktopdir}/kde/krdc.desktop
%{_desktopdir}/kde/krfb.desktop
%{_desktopdir}/kde/kcmkrfb.desktop
%{_iconsdir}/*/*/*/krdc*
%{_iconsdir}/[!l]*/*/*/krfb*

%files ksirc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirc
%attr(755,root,root) %{_bindir}/dsirc
%{_libdir}/ksirc.la
%attr(755,root,root) %{_libdir}/ksirc.so
%{_libdir}/libkntsrcfilepropsdlg.la
%attr(755,root,root) %{_libdir}/libkntsrcfilepropsdlg.so
%{_desktopdir}/kde/ksirc.desktop
%{_datadir}/config/ksircrc
%{_datadir}/apps/ksirc
%{_datadir}/services/kntsrcfilepropsdlg.desktop
%{_iconsdir}/[!l]*/*/*/ksirc*

%files ktalkd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/k*talkd*
%{_libdir}/kde3/kcm_ktalkd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_ktalkd.so
%{_datadir}/config/ktalkd*
%{_datadir}/sounds/ktalkd*
%{_iconsdir}/*/*/*/ktalkd*
%{_desktopdir}/kde/kcmktalkd.desktop

%files ktnef
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktnef
%{_libdir}/libktnef.la
%attr(755,root,root) %{_libdir}/libktnef.so.*
%{_iconsdir}/*/*/*/ktnef*


%files kxmlrpcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kxmlrpcd
%{_libdir}/kxmlrpcd.la
%attr(755,root,root) %{_libdir}/kxmlrpcd.so
%{_libdir}/kde3/kcm_xmlrpcd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_xmlrpcd.so
%{_datadir}/services/kxmlrpcd.desktop

%files lanbrowser
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lisarc
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/lisa
%attr(754,root,root) /etc/rc.d/init.d/lisa
%attr(755,root,root) %{_bindir}/lisa
%attr(755,root,root) %{_bindir}/reslisa
%{_libdir}/kde3/kio_lan.la
%attr(755,root,root) %{_libdir}/kde3/kio_lan.so
%{_libdir}/kde3/kcm_lanbrowser.la
%attr(755,root,root) %{_libdir}/kde3/kcm_lanbrowser.so
%{_datadir}/services/rlan.protocol
%{_datadir}/services/lan.protocol
%{_datadir}/apps/lisa
%{_datadir}/apps/konqueror/dirtree/remote/lan.desktop
%{_datadir}/applnk/.hidden/kcmkiolan.desktop
%{_datadir}/applnk/.hidden/kcmlisa.desktop
%{_datadir}/applnk/.hidden/kcmreslisa.desktop
