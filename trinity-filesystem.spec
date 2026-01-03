# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 4

%define tde_prefix /opt/trinity


Name:		trinity-filesystem
Version:	%{tde_version}
Release:	%{pkg_rel}
Summary:	Trinity Directory Layout
Group:		System/Fhs
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

# BuildArch:	noarch


%description
This package installs the Trinity directory structure.


%files
%defattr(-,root,root,-)
%{_sysconfdir}/ld.so.conf.d/tde.conf

%dir %{tde_prefix}

%dir %{tde_prefix}/bin

%dir %{tde_prefix}/share
%dir %{_sysconfdir}/trinity/magic

%dir %{tde_prefix}/share/doc
%dir %{tde_prefix}/share/doc/tde
%dir %{tde_prefix}/share/doc/tde/HTML
%dir %{tde_prefix}/share/doc/tde/HTML/*
%dir %{tde_prefix}/share/doc/tde/HTML/*/common

%dir %{tde_prefix}/include
%dir %{tde_prefix}/include/tde

%dir %{tde_prefix}/%{_lib}
%dir %{tde_prefix}/%{_lib}/java
%dir %{tde_prefix}/%{_lib}/jni
%dir %{tde_prefix}/%{_lib}/pkgconfig
%dir %{tde_prefix}/%{_lib}/trinity

%dir %{tde_prefix}/share/applications
%dir %{tde_prefix}/share/applications/tde
%dir %{tde_prefix}/share/applnk
%dir %{tde_prefix}/share/applnk/.hidden
%dir %{tde_prefix}/share/applnk/*
%dir %{tde_prefix}/share/applnk/*/*
%dir %{tde_prefix}/share/apps
%dir %{tde_prefix}/share/apps/*
%dir %{tde_prefix}/share/apps/*/*
%dir %{tde_prefix}/share/cmake
%dir %{tde_prefix}/share/config.kcfg
%dir %{tde_prefix}/share/autostart
%dir %{tde_prefix}/share/emoticons
%dir %{tde_prefix}/share/icons
%dir %{tde_prefix}/share/icons/crystalsvg
%dir %{tde_prefix}/share/icons/crystalsvg/*
%dir %{tde_prefix}/share/icons/crystalsvg/*/*
%dir %{tde_prefix}/share/icons/hicolor
%dir %{tde_prefix}/share/icons/hicolor/*
%dir %{tde_prefix}/share/icons/hicolor/*/*
%dir %{tde_prefix}/share/icons/locolor
%dir %{tde_prefix}/share/icons/locolor/*
%dir %{tde_prefix}/share/icons/locolor/*/*
%dir %{tde_prefix}/share/locale
%dir %{tde_prefix}/share/locale/*
%dir %{tde_prefix}/share/locale/*/*
%dir %{tde_prefix}/share/man
%dir %{tde_prefix}/share/man/*
%dir %{tde_prefix}/share/mime
%dir %{tde_prefix}/share/mime/*
%dir %{tde_prefix}/share/mimelnk
%dir %{tde_prefix}/share/mimelnk/*
%dir %{tde_prefix}/share/services
%dir %{tde_prefix}/share/services/*
%dir %{tde_prefix}/share/servicetypes
%dir %{tde_prefix}/share/tdestyle
%dir %{tde_prefix}/share/tdestyle/*
%dir %{tde_prefix}/share/X11
%dir %{tde_prefix}/share/X11/xkb
%dir %{tde_prefix}/share/X11/xkb/symbols

%dir %{tde_prefix}/share/wallpapers


%dir %{_sysconfdir}/trinity
%dir %{_sysconfdir}/xdg/menus

##########

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/

echo "/opt/trinity/%{_lib}" > tde.conf

%__install -p -c -m 644 tde.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/tde.conf
%__install -d -m 755 %{?buildroot}%{tde_prefix}

%__install -d -m 755 %{?buildroot}%{tde_prefix}/bin

%__install -d -m 755 %{?buildroot}%{tde_prefix}/share
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applications
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applications/tde
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/.hidden
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Applications
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Development
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Edutainment
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Edutainment/Languages
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Edutainment/Mathematics
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Edutainment/Miscellaneous
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Edutainment/Science
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Edutainment/Tools
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Games
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Games/Board
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Graphics
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Internet
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Multimedia
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Office
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Settings
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Settings/LookNFeel
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Settings/WebBrowsing
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/System
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/System/ScreenSavers
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Toys
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/applnk/Utilities
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/plugin
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/profiles
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/remotes
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/remoteview
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/tdedisplay
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/tdedisplay/color-schemes
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/videothumbnail
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/apps/zeroconf
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/autostart
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/cmake
%__install -d -m 755 %{?buildroot}%{_sysconfdir}/trinity
%__install -d -m 755 %{?buildroot}%{_sysconfdir}/trinity/magic
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/config.kcfg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/emoticons
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man1
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man2
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man3
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man4
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man5
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man6
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man7
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man8
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/man/man9
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mime
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mime/packages
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/all
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/application
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/audio
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/fonts
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/image
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/interface
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/inode
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/media
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/message
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/model
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/multipart
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/print
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/text
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/uri
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/mimelnk/video
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/services
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/services/tdeconfiguredialog
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/servicetypes
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/tdestyle
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/tdestyle/themes
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/X11/xkb/symbols

%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/wallpapers

# Create icons directories
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/icons
for t in crystalsvg hicolor locolor ; do
  %__install -d -m 755 "%{?buildroot}%{tde_prefix}/share/icons/${t}"
  %__install -d -m 755 "%{?buildroot}%{tde_prefix}/share/icons/${t}/scalable"
  for i in {16,22,32,48,64,128,256} ; do
    %__install -d -m 755 "%{?buildroot}%{tde_prefix}/share/icons/${t}/${i}x${i}"
  done

  # Create subdirectories
  for r in actions apps categories devices mimetypes places ; do
    %__install -d -m 755 "%{?buildroot}%{tde_prefix}/share/icons/${t}/scalable/${r}"
    for i in {16,22,32,48,64,128} ; do
      %__install -d -m 755 "%{?buildroot}%{tde_prefix}/share/icons/${t}/${i}x${i}/${r}"
    done
  done
done

%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde

# HTML directories
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/ca/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/cs/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/da/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/de/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en_GB/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/es/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/et/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/fi/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/fr/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/gl/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/he/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/hu/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/it/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/ja/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/nl/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/pl/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/pt_BR/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/pt/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/ro/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/ru/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/sk/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/sl/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/sr/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/sr@Latn/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/sv/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/tr/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/uk/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/zh_CN/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/zh_Hans/common
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/zh_TW/common

%__install -d -m 755 %{?buildroot}%{tde_prefix}/include
%__install -d -m 755 %{?buildroot}%{tde_prefix}/include/tde

%__install -d -m 755 %{?buildroot}%{tde_prefix}/%{_lib}
%__install -d -m 755 %{?buildroot}%{tde_prefix}/%{_lib}/java
%__install -d -m 755 %{?buildroot}%{tde_prefix}/%{_lib}/jni
%__install -d -m 755 %{?buildroot}%{tde_prefix}/%{_lib}/pkgconfig
%__install -d -m 755 %{?buildroot}%{tde_prefix}/%{_lib}/trinity

%__install -d -m 755 %{?buildroot}%{_sysconfdir}/trinity
%__install -d -m 755 %{?buildroot}%{_sysconfdir}/xdg/menus

# Locales directories
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/en_US
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/C
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ad
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ae
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/af
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ag
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ai
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/al
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/am
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/an
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ao
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ar
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/as
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/at
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/au
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/aw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ax
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/az
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ba
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bb
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bd
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/be
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bf
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bh
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bi
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bj
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bo
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/br
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/braille
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bs
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bt
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/by
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/bz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ca
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cd
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cf
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ch
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ci
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ck
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cl
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/co
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cu
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cv
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cx
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cy
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/cz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/de
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/dj
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/dk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/dm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/do
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/dz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ec
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ee
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/eg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/eh
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/eo
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/er
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/es
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/et
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/fi
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/fj
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/fk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/fm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/fo
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/fr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ga
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gb
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gd
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ge
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gh
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gi
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gl
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gp
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gq
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gt
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gu
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/gy
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/hk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/hn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/hr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ht
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/hu
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/id
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ie
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/il
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/in
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/iq
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ir
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/is
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/it
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/jm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/jo
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/jp
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/jv
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ke
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/kg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/kh
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ki
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/km
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/kn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/kp
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/kr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/kw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ky
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/kz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/la
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/lb
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/lc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/li
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/lk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/lr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ls
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/lt
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/lu
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/lv
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ly
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ma
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/md
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/me
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mh
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mi
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ml
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mo
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mq
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ms
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mt
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mu
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mv
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mx
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/my
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/mz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/na
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/nc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ne
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/nf
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ng
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ni
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/nl
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/no
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/np
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/nr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/nu
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/nz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/om
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pa
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pe
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pf
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ph
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pl
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ps
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pt
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/pw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/py
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/qa
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ro
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/rs
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ru
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/rw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sa
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sb
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sd
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/se
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sh
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/si
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/so
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/st
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sv
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sy
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/sz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/td
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/th
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tj
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tk
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/to
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tp
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tr
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tt
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tv
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tw
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/tz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ua
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ug
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/us
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/uy
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/uz
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/va
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/vc
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ve
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/vg
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/vi
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/vn
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/vu
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/wf
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ws
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/ye
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/za
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/zm
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/l10n/zw

# Directories for LC_MESSAGES (from *-i18n packages)
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/af/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ar/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/az/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/be/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/bg/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/bn/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/br/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/bs/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ca/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ca@valencia/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/cs/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/csb/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/cy/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/da/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/de/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/du/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ee/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/el/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/en/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/en_GB/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/en_US/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/eo/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/es/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/es_AR/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/et/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/eu/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/fa/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/fi/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/fo/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/fr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/fy/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ga/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/gl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/gu/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/he/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/hi/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/hr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/hu/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/id/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/is/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/it/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ja/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ka/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/kk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/km/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ko/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ku/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/lo/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/lt/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/lv/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/mk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/mr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ms/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/mt/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/nb/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/nds/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ne/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/nl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/nn/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/nso/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/pa/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/pl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/pl_PL/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/pl-utf/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/pt/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/pt_PT/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/pt_BR/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ro/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ru/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/rw/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/se/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/si/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sl/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sl_SI/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sq/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sr@latin/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sr@Latn/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ss/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/sv/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ta/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/tg/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/th/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/tr/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ug/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/uk/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/uk@cyrillic/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/uz/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/uz@cyrillic/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ve/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/ven/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/vi/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/wa/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/xh/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/xx/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/zh_CN.GB2312/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/zh_CN/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/zh_Hans/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/zh_Hant/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/zh_TW.Big5/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/zh_TW/LC_MESSAGES/
%__install -d -m 755 %{?buildroot}%{tde_prefix}/share/locale/zu/LC_MESSAGES/

%post -p /usr/bin/ldconfig

%postun -p /usr/bin/ldconfig

