INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_KYLE kyle)

FIND_PATH(
    KYLE_INCLUDE_DIRS
    NAMES kyle/api.h
    HINTS $ENV{KYLE_DIR}/include
        ${PC_KYLE_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    KYLE_LIBRARIES
    NAMES gnuradio-kyle
    HINTS $ENV{KYLE_DIR}/lib
        ${PC_KYLE_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(KYLE DEFAULT_MSG KYLE_LIBRARIES KYLE_INCLUDE_DIRS)
MARK_AS_ADVANCED(KYLE_LIBRARIES KYLE_INCLUDE_DIRS)

