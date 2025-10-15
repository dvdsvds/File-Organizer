#include <pybind11/pybind11.h>
#include <iostream>
#include <filesystem>
#include <map>
#include <string>

namespace py = pybind11;
namespace fs = std::filesystem;

struct CategoryGroup {
    std::string name;
    std::vector<std::string> exts;
};

std::vector<CategoryGroup> group = {
    {"Images", {".png", ".jpg", ".jpeg", ".gif", ".tiff", ".psd", ".pdd", ".swi", ".fla", ".bmp"}},
    {"Documents", {".xls", ".xlsx", ".ppt", ".pptx", ".doc", ".docx", ".pdf", ".ai", ".hwp", ".txt"}},
    {"Media", {".mp3", ".mp4", ".wav", ".wma", ".mid", ".mkv", ".avi", ".flv", ".mov"}},
    {"Archives", {".7z", ".xz", ".gzip", ".tar", ".zip", ".wim", ".alz", ".egg", ".rar"}},
    {"execute", {".exe"}}
};

std::string toLowerString(std::string ext) {
    std::transform(ext.begin(), ext.end(), ext.begin(), [](unsigned char c){return std::tolower(c);});
    return ext;
}

void search(const fs::path& folder_path, const std::vector<CategoryGroup>& group) {
    for(const auto& entry : fs::directory_iterator(folder_path)) {
        if(entry.is_directory()) {
            bool skip = false;
            std::string folder = entry.path().filename().string();
            for(const auto& g : group) {
                if(folder == g.name) {
                    skip = true;
                    break;
                }
            }
            if(skip) continue;

            search(entry.path(), group);

        } else if(entry.is_regular_file()) {
            std::string exts = toLowerString(entry.path().extension().string());
            
            for(const auto& g : group) {
                if(std::find(g.exts.begin(), g.exts.end(), exts) != g.exts.end()) {
                    std::string folderName = exts;
                    if(!folderName.empty() && folderName[0] == '.')  folderName.erase(0, 1); 

                    fs::path dest = folder_path / g.name / folderName;
                    fs::create_directories(dest);

                    fs::path newPath = dest / entry.path().filename();

                    try {
                        fs::rename(entry.path(), newPath);
                    } catch(const fs::filesystem_error& error) {
                        std::cerr << "Failed:" << error.what() << std::endl;
                        continue;
                    }

                    break;
                }
            }
        }
    }
}

void organize(const std::string& folder_path) {
    if(!(fs::exists(folder_path) && fs::is_directory(folder_path))) {
        std::cout << folder_path << " is not exists." << std::endl;
    }
    search(fs::path(folder_path), group);
}

PYBIND11_MODULE(fileorganizer, m) {
    m.doc() = "File Organizer Module (C++ -> Python)";
    m.def("organize", &organize, "Organize files by category", py::arg("folder_path"));
}