Summary:	GNOME/GTK+ integration of special directories
Name:		xdg-user-dirs-gtk
Version:	0.6
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/xdg-user-dirs-gtk/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	fdc72260fc53c3ce5c49f205a0b627e8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	xdg-user-dirs
Requires:	xdg-user-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-user-dirs-gtk is a companion to xdg-user-dirs that integrates it
into the GNOME desktop and GTK+ applications.

It gets run during login and does two things:
* Tracks changes of locale and prompts the user so the directories
  can be changed.
* Creates a default gtk bookmarks file if there is none, based
  on a set of xdg user dirs.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xdg-user-dirs-gtk-update
%{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop
