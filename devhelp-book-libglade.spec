Summary:	DevHelp book: libglade
Summary(pl):	Ksi±¿ka do DevHelpa o libglade
Name:		devhelp-book-libglade
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.devhelp.net/books/books/libglade.tar.gz
URL:		http://www.devhelp.net/
Requires:	devhelp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
DevHelp book about libglade.

%description -l pl
Ksi±¿ka do DevHelpa o libglade.

%prep
%setup -q -c -n libglade

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{books/libglade,specs}

install book.devhelp $RPM_BUILD_ROOT%{_prefix}/specs/libglade.devhelp
install book/* $RPM_BUILD_ROOT%{_prefix}/books/libglade

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_prefix}/books/*
%{_prefix}/specs/*
