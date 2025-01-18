Summary:	GNOME/GTK+ integration of special directories
Summary(pl.UTF-8):	Integracja specjalnych katalogów z GNOME/GTK+
Name:		xdg-user-dirs-gtk
Version:	0.13
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/xdg-user-dirs-gtk/0.13/%{name}-%{version}.tar.xz
# Source0-md5:	7ed574239197662226eeb5980ba9ec94
Patch0:		mate-support.patch
URL:		https://gitlab.gnome.org/GNOME/xdg-user-dirs-gtk
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xdg-user-dirs
BuildRequires:	xz
Requires:	xdg-user-dirs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-user-dirs-gtk is a companion to xdg-user-dirs that integrates it
into the GNOME desktop and GTK+ applications.

It gets run during login and does two things:
- Tracks changes of locale and prompts the user so the directories can
  be changed.
- Creates a default GTK+ bookmarks file if there is none, based on a
  set of xdg user dirs.

%description -l pl.UTF-8
xdg-user-dirs-gtk to pakiet towarzyszący xdg-user-dirs, integrujący go
ze środowiskiem GNOME i aplikacjami GTK+.

Jest uruchamiany podczas logowania i wykonuje dwie czynności:
- śledzi zmiany lokalizacji i proponuje użytkownikowi zmianę katalogów
- tworzy domyślny plik zakładek GTK+ (jeśli go nie ma) w oparciu o
  zestaw katalogów użytkownika xdg.

%prep
%setup -q
%patch -P0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xdg-user-dirs-gtk-update
%{_desktopdir}/user-dirs-update-gtk.desktop
%{_sysconfdir}/xdg/autostart/user-dirs-update-gtk.desktop
