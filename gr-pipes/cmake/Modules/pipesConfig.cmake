INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PIPES pipes)

FIND_PATH(
    PIPES_INCLUDE_DIRS
    NAMES pipes/api.h
    HINTS $ENV{PIPES_DIR}/include
        ${PC_PIPES_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PIPES_LIBRARIES
    NAMES gnuradio-pipes
    HINTS $ENV{PIPES_DIR}/lib
        ${PC_PIPES_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PIPES DEFAULT_MSG PIPES_LIBRARIES PIPES_INCLUDE_DIRS)
MARK_AS_ADVANCED(PIPES_LIBRARIES PIPES_INCLUDE_DIRS)

